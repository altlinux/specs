%define _unpackaged_files_terminate_build 1

Name: eyeD3
Version: 0.8.11
Release: alt1

Summary: Console tool that displays and manipulates id3-tags on mp3 files
License: GPLv2+
Group: Sound
URL: http://eyed3.nicfit.net
BuildArch: noarch

Source0: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
Requires: python3-module-%name = %EVR


%description
eyeD3 manipulates ID3 tags in mp3 files and is able to read/write and
convert between ID3 v1.0, v1.1, v2.3 and v2.4 tags. High-level access
is provided to most frames, including APIC (i.e., images) frames.

%package -n python3-module-%name
Summary: A python module for processing mp3 files
Group: Development/Python3

%description -n python3-module-%name
eyeD3 is a Python module and program for processing ID3 tags.
Information about mp3 files (i.e bit rate, sample frequency,
play time, etc.) is also provided.  The formats supported are ID3
v1.0/v1.1 and v2.3/v2.4.

This module is built for python %_python_version

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
export CFLAGS="%optflags"
%python3_build

%install
export CFLAGS="%optflags"
%python3_install

%files
%doc *.rst docs/ examples/
%_bindir/*

%files -n python3-module-%name
%python3_sitelibdir/*


%changelog
* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.8.11-alt1
- Version updated to 0.8.11
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.7.4-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt1
- Version 0.7.4
- Added module for Python 3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.17-alt1.1
- Rebuild with Python-2.7

* Thu Aug 26 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.6.17-alt1
- 0.6.17
- spec fixes

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.15-alt1.1
- Rebuilt with python 2.6

* Sun May 04 2008 Eugene Vlasov <eugvv@altlinux.ru> 0.6.15-alt1
- New version
- Fixed frames.py variable names misprints

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.6.14-alt1.1
- Rebuilt with python-2.5.

* Wed May 09 2007 Eugene Vlasov <eugvv@altlinux.ru> 0.6.14-alt1
- New version

* Tue May 01 2007 Eugene Vlasov <eugvv@altlinux.ru> 0.6.13-alt1
- New version

* Wed Feb 28 2007 Eugene Vlasov <eugvv@altlinux.ru> 0.6.12-alt1
- New version

* Sun Nov 26 2006 Eugene Vlasov <eugvv@altlinux.ru> 0.6.11-alt1
- New version
- Fixed build on x86_64

* Fri May 05 2006 Eugene Vlasov <eugvv@altlinux.ru> 0.6.10-alt1
- New version
- Fix for work with invalid WXXX frames merged in upstream
- Minor spec fixes

* Sat Feb 04 2006 Eugene Vlasov <eugvv@altlinux.ru> 0.6.9-alt2
- Fixed work with invalid WXXX frames
- Fixed unpackaged files warning

* Sun Jan 08 2006 Eugene Vlasov <eugvv@altlinux.ru> 0.6.9-alt1
- New version
- Patch for new tag linking merged in upstream

* Sun Oct 16 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.6.8-alt2
- Fixed new tag linking

* Tue Aug 30 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.6.8-alt1
- New version, critical bug fixed

* Sun Aug 28 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.6.7-alt1
- New version

* Thu May 19 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.6.6-alt1
- New version

* Tue Apr 19 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.6.5-alt1
- New version

* Sat Mar 12 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.6.4-alt3
- Rebuild with python 2.4

* Mon Feb 14 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.6.4-alt2
- Fixed work with incorrect TYER frames

* Mon Feb 07 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.6.4-alt1
- New version

* Fri Nov 26 2004 Eugene Vlasov <eugvv@altlinux.ru> 0.6.3-alt1
- First build for Sisyphus

