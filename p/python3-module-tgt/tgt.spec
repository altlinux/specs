%define oname tgt

Name: python3-module-%oname
Version: 1.4.3
Release: alt2

Summary: Read, write, and manipulate Praat TextGrid files
License: BSD
Group: Development/Python3
Url: http://github.com/hbuschme/TextGridTools/
Buildarch: noarch

Source: tgt-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
TextGridTools -- Read, write, and manipulate Praat TextGrid files with

%prep
%setup -n %oname-%version

## py2 -> py3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
##

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*%{oname}*
%_bindir/*


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4.3-alt2
- python2 -> pyhton3

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

