#/bin/bash
main() {
    wks-read --debug QPGS0 QPIGS Q1 >> out.log 2>&1
    echo "\n---------------------------------------\n" >> out.log
    sleep 10
    main
}

main
