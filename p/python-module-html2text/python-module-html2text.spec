Name: python-module-html2text
Version: 3.200.3
Release: alt1

Summary: Converts a page of HTML into clean, easy-to-read plain ASCII text
Group: Development/Python
License: GPLv3+
Url: http://www.aaronsw.com/2002/html2text/
BuildArch: noarch

%setup_python_module html2text

BuildRequires: python-module-distribute

# https://github.com/aaronsw/html2text
# git://git.altlinux.org/gears/p/%name.git
Source: %name-%version-%release.tar

%description
html2text is a Python script that convers a page of HTML into clean,
easy-to-read plain ASCII text.  Better yet, that ASCII also happens to
be valid Markdown (a text-to-HTML format).

%prep
%setup -n %name-%version-%release
sed -i '/^sys\.path\.insert/d' test/run_tests.py

%install
mkdir -p %buildroot{%python_sitelibdir,%_bindir}
install -pm644 html2text.py %buildroot%python_sitelibdir/
r="$(realpath --relative-to=%_bindir %python_sitelibdir/html2text.py)"
ln -s -- "$r" %buildroot%_bindir/

%check
cd test
PYTHONPATH=%buildroot%python_sitelibdir %__python run_tests.py

%files
%_bindir/html2text.py
%python_sitelibdir/html2text.py?
%attr(755,root,root) %python_sitelibdir/html2text.py

%changelog
* Wed Apr 03 2013 Dmitry V. Levin <ldv@altlinux.org> 3.200.3-alt1
- Updated to 3.200.3-60-g8ddc844.

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.37-alt1.1
- Rebuild with Python-2.7

* Mon Feb 01 2010 Dmitry V. Levin <ldv@altlinux.org> 2.37-alt1
- Initial revision.
