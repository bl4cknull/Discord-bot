import subprocess
import re

zerosign= """     @@@@@@@@ @@@@@@@@ @@@@@@@   @@@@@@       @@@@@@@  @@@       @@@@@@   @@@@@@@ @@@  @@@
          @@! @@!      @@!  @@@ @@!  @@@      @@!  @@@ @@!      @@!  @@@ !@@      @@!  !@@
        @!!   @!!!:!   @!@!!@!  @!@  !@!      @!@!@!@  @!!      @!@!@!@! !@!      @!@@!@!
      !!:     !!:      !!: :!!  !!:  !!!      !!:  !!! !!:      !!:  !!! :!!      !!: :!!
     :.::.: : : :: :::  :   : :  : :. :       :: : ::  : ::.: :  :   : :  :: :: :  :   :::
                                                                                          """

def datas(link):
    subprocesses = subprocess.Popen(
        "docker run -ti --rm theharvester:latest -d " + link + " -b bing",
        shell=True,
        stdout=subprocess.PIPE,
    )
    arr = []
    subprocess_return = subprocesses.stdout.read().decode('utf-8')
    text = '\n'.join(subprocess_return.split('\n')[27:])
    f = open('result.txt','w')
    f.write(text)
    if not len(text) > 25:
        f.write("{}\n\n\n\t\t\tResult not found".format(zerosign))
    return text


