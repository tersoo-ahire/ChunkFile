csvfile = "dhis2database.csv"

row_size = 100  # how many rows the user wants in each split file

def main():
    
    #creates the chunk files and writes to it
    def write_chunk(part, lines):
        with open('dhis2database'+ str(part) +'.csv', 'w') as f_out:
            f_out.write(header)
            f_out.writelines(lines)
            
    with open("dhis2database.csv", 'r') as f:
        count = 0
        header = f.readline()
        lines = []
        for line in f:
            count += 1
            lines.append(line)
            if count % row_size == 0:
                write_chunk(count // row_size, lines)
                lines = []
        # write remainder
        if len(lines) > 0:
            write_chunk((count // row_size) + 1, lines)
if __name__ == '__main__':
    main()