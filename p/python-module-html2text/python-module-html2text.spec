Name: python-module-html2text
Version: 2.37
Release: alt1.1

%define sname html2text

Summary: Converts a page of HTML into clean, easy-to-read plain ASCII text
Group: Development/Python
License: GPLv3+
Url: http://www.aaronsw.com/2002/html2text/
BuildArch: noarch

%setup_python_module html2text

# http://www.aaronsw.com/2002/html2text/%sname-%version.py
Source: %sname.py

%description
html2text is a Python script that convers a page of HTML into clean,
easy-to-read plain ASCII text.  Better yet, that ASCII also happens to
be valid Markdown (a text-to-HTML format).

%install
mkdir -p %buildroot%python_sitelibdir
sed 's/\r//' <%_sourcedir/%sname.py >%buildroot%python_sitelibdir/%sname.py

%files
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.37-alt1.1
- Rebuild with Python-2.7

* Mon Feb 01 2010 Dmitry V. Levin <ldv@altlinux.org> 2.37-alt1
- Initial revision.
