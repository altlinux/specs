Name: ALDConvert
Version: 0.06
%define tstamp 08062912
Release: alt2.1.1
BuildArch: noarch
Packager: Fr. Br. George <george@altlinux.ru>

Summary: ALT Linux Documentation Project format converter
Summary(ru_RU.KOI8-R): Преобразователь текстовых форматов для ALT Linux Documentation Project
Group: Text tools
License: BSD

Source: http://phobos.cs.msu.su/~george/Download/%name.%tstamp.tar.gz

Requires: python-module-tpg > 3.0

BuildRequires: python-module-tpg > 3.0

%description
A tool for converting between various text formats accepted by ALT Linux Documentation Project.
Supported input formats: M-K
Supported output formats: HTML, laTeX, Moin-Moin

%description -l ru-RU.KOI8-R
Утилита-конвертор разнообразных текстовых форматов для ALT Linux Documentation Project
Поддерживаемые входные форматы: M-K
Поддерживаемые выходные форматы: HTML, laTeX, Moin-Moin

%prep
%setup -n %{name}

%build
make metalexer.py
make
make Format_Quick.html
make Makefile.production DST="/usr"

%install
make install DST="$RPM_BUILD_ROOT/usr/"
#%__mkdir_p "$RPM_BUILD_ROOT/%_libdir"

%files
%doc Format_Quick.html picture.gif
%_bindir/%name
/usr/libexec/%name/
/usr/libexec/%{name}_g/

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.06-alt2.1.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.06-alt2.1
- Rebuilt with python 2.6

* Wed Aug 27 2008 Fr. Br. George <george@altlinux.ru> 0.06-alt2
- More 1.6+ syntax fixes

* Sun Aug 24 2008 Fr. Br. George <george@altlinux.ru> 0.06-alt1
- MoinMoin 1.6+ syntax added

* Sun Jun 29 2008 Fr. Br. George <george@altlinux.ru> 0.05-alt10
- Non-posix 'tail +3' removed
- New mktemp wants not any symbols after XXX, fixed

* Fri Mar 07 2008 Fr. Br. George <george@altlinux.ru> 0.05-alt9
- HTML generator typo fix

* Thu Sep 14 2006 Fr. Br. George <george@altlinux.ru> 0.05-alt8
- GEAR adaptation
- minor docs changes
- stdout->stderr redirection fixed

* Sun Aug 20 2006 Fr. Br. George <george@altlinux.ru> 0.05-alt7
- Quick user documentation is ready now

* Thu Jun 01 2006 Fr. Br. George <george@altlinux.ru> 0.05-alt6
- Noarch build

* Sat May 13 2006 Fr. Br. George <george@altlinux.ru> 0.05-alt5
- some BR and FR implemented

* Mon Mar 20 2006 Fr. Br. George <george@altlinux.ru> 0.05-alt4
- New snapshot with id=9287 fixed

* Thu Mar 09 2006 Fr. Br. George <george@altlinux.ru> 0.05-alt3
- Further bugfixes

* Wed Feb 08 2006 Fr. Br. George <george@altlinux.ru> 0.05-alt2
- some parser bugs in m-k

* Sat Feb 04 2006 Fr. Br. George <george@altlinux.ru> 0.05-alt1
- color marks, tables etc. in m-k

* Thu Dec 29 2005 Fr. Br. George <george@altlinux.ru> 0.04-alt9
- Small latex writer improvement

* Fri Dec 16 2005 Fr. Br. George <george@altlinux.ru> 0.04-alt8
- Many m-k bugfixes 

* Sun Nov 13 2005 Fr. Br. George <george@altlinux.ru> 0.04-alt7
- Charset recoding added

* Wed Oct 12 2005 Fr. Br. George <george@altlinux.ru> 0.04-alt6
- Small fixes

* Fri Sep 30 2005 Fr. Br. George <george@altlinux.ru> 0.04-alt4
- Many laTeX writer chanes

* Thu Sep 29 2005 Fr. Br. George <george@altlinux.ru> 0.04-alt3
- Many bugzilla/gc issues

* Fri Sep 23 2005 Fr. Br. George <george@altlinux.ru> 0.04-alt2
- M-K reader improved

* Fri Sep 09 2005 Fr. Br. George <george@altlinux.ru> 0.04-alt1
- Next version. Moin-Moin writer

* Sat Sep 03 2005 Fr. Br. George <george@altlinux.ru> 0.03-alt1
- Next version, external readers are supported 

* Sat Aug 27 2005 Fr. Br. George <george@altlinux.ru> 0.02-alt1
- Next version, development in progress:)

* Fri Jun 24 2005 Fr. Br. George <george@altlinux.ru> 0.01-alt1
- Initial build

