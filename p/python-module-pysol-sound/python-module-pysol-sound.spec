# -*- coding: utf-8 -*-

%define version 3.01
%define release alt3
%setup_python_module pysol-sound

Name: %packagename
Version: %version
Release: %release.1

Summary: Sound server for pysol
Summary(ru_RU.UTF-8): Поддержка звука для PySol
License: GPL
Group: Games/Cards
Packager: Eugene Vlasov <eugvv@altlinux.ru>
URL: http://www.oberhumer.com/opensource/pysol/

Source: %modulename-server-%version.tar.bz2


# Automatically added by buildreq on Wed Mar 30 2005
BuildRequires: libSDL-devel libsmpeg-devel python-devel python-modules-encodings

Provides: pysol-sound-server = %version-%release
Obsoletes: pysol-sound-server <= 3.00-alt4

%description
Pysol-sound-server - Python extension module that plays WAV samples
together with MP3 or MOD background music.

This module is built for python %__python_version

%description -l ru_RU.UTF-8
Pysol-sound-server - расширение Python для воспроизведения звуков WAV
вместе с фоновой музыкой в формате MP3 или MOD

Этот модуль собран для Python версии %__python_version

%prep
%setup -n %modulename-server-%version

%build
(cd src
./configure
%python_build_debug
)

%install
(cd src
%python_install
)

%files
%python_sitelibdir/pysol*
%doc README NEWS

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.01-alt3.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.01-alt3
- Rebuilt for debuginfo

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.01-alt2
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 3.01-alt1.1
- Rebuilt with python-2.5.

* Wed Mar 30 2005 Eugene Vlasov <eugvv@altlinux.ru> 3.01-alt1
- New version
- Fixed python policy compatibility
- Rebuild with python2.4

* Thu May 20 2004 Alexei Takaseev <taf@altlinux.ru> 3.00-alt4
- fix buildrequires: python23-devel -> python-dev

* Sun Dec 07 2003 Alexei Takaseev <taf@altlinux.ru> 3.00-alt3
- rebuild with python23

* Wed Oct 29 2003 Alexei Takaseev <taf@altlinux.ru> 3.00-alt2
- It is taken back from orphaned

* Tue Aug 13 2002 Stanislav Ievlev <inger@altlinux.ru> 3.00-alt1
- first release for ALT

