# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from proxypool.scheduler import Scheduler
import sys
import io
from lxml import etree

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    try:
        s = Scheduler()
        s.run()
    except:
        main()


if __name__ == '__main__':
    main()
