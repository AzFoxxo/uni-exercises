%{
    // Includes (libraries)
    #include <stdio.h>
    #include <stdbool.h>
    #include <string.h>

    // Function forward declarations
    int yylex (void);
    extern int yyparse();
    void yyerror (char const *);
    void display_boolean(bool result);
    void display_help_message();
%}

%define api.value.type {char}

%token BOOLEAN
%token AND
%token OR
%token NOT
%token XOR
%token NL
%start INPUT

%%
INPUT:
    %empty
    | INPUT NL { display_boolean($1); }
    | INPUT EXPRESSION NL { display_boolean($2); }
;

EXPRESSION:
    BOOLEAN
    | EXPRESSION EXPRESSION OR { $$ = $1 || $2; }
    | EXPRESSION EXPRESSION AND { $$ = $1 && $2; }
    | EXPRESSION NOT { $$ = !$1; }
    | EXPRESSION EXPRESSION XOR { $$ = $1 ^ $2; }
    ;

%%

// Entry point
int main(int argc, char **argv) {
    puts("Basic Boolean Calculator");

    // Check if help flag was provided
    if (argc > 1 && strcmp(argv[1], "help") == 0) {
        display_help_message();
        return 0;
    }

    // Parse the input continuously
    while (true) {
        yyparse();

        // Control + D to exit
        if (feof(stdin)) break;
    }

    return 0;
}

// Display help message
inline void display_help_message() {
    puts("Help page:");
    puts("The boolean calculator uses postfix notation.");
    puts("E.g. TRUE FALSE &");
    puts("Operands:");
    puts("\t1/true or t (case insensitive) - TRUE");
    puts("\t0/false or f (case insensitive) - FALSE");
    puts("Operators:");
    puts("\t| or OR (case insensitive) - OR operator");
    puts("\t& or AND (case insensitive)  - AND operator");
    puts("\t’ or NOT (case insensitive)  - NOT operator");
    puts("\t^ or XOR (case insensitive)  - XOR operator");
    puts("Hit enter to evaluate the provided expression.");
}

// Illegal character/expression
void yyerror (char const *s) {
    puts("ILLEGAL EXPRESSION!");

    int token;
    while ((token = yylex()) != NL && token != 0) { /* Skip line */ } 
}

// Display results of binary operation to the console
inline void display_boolean(bool result) {
    if (result) puts("TRUE"); else puts("FALSE");
}
