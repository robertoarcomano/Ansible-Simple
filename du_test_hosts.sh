ansible tests -i tests/inventory -m shell -a "du -s /var/spool/*|sort -n"
