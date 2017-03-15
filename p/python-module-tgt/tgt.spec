Name: python-module-tgt
Version: 1.4.3
Release: alt1
Summary: Read, write, and manipulate Praat TextGrid files
License: BSD
Group: Development/Python
Url: http://github.com/hbuschme/TextGridTools/
Source: tgt-%version.tar.gz
Buildarch: noarch

%setup_python_module tgt

%description
TextGridTools -- Read, write, and manipulate Praat TextGrid files with

%prep
%setup -n tgt-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*tgt*
%_bindir/*

%changelog
* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 1.4.3-alt1
- Autobuild version bump to 1.4.3

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 1.4.2-alt1
- Autobuild version bump to 1.4.2

* Wed Jan 13 2016 Fr. Br. George <george@altlinux.ru> 1.3.1-alt1
- Autobuild version bump to 1.3.1

* Wed Apr 22 2015 Fr. Br. George <george@altlinux.ru> 1.2.0-alt1
- Autobuild version bump to 1.2.0

* Thu Apr 10 2014 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

* Thu Apr 10 2014 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from scratch

