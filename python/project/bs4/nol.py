import urllib.request as urlreq
import urllib.parse as urlpar

# 1: Read Beautiful soup doc and import it

def getNolUrl(course, year, term, page):
    main_url = 'https://nol.ntu.edu.tw/nol/coursesearch/search_result.php?'

    # 2: Modify the qry string
    # Hint: urllib.parse.quote may be helpful
    get_qry = 'alltime=yes&allproced=yes&cstype=2&csname=%B4%B6' \
            '&current_sem=103-1&startrec=0'

    return main_url + get_qry


course_name = '普'.encode('big5')
nolUrl = getNolUrl(course_name, 103, 1, 0)

# 3: Get url data

# You could see if you suceed
print(soup.prettify())


# 4: Find the table
# x.find_all('child') will return a list of all child with tag name 'child'

# 5: Print the data !
