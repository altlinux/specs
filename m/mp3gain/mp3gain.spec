Name: mp3gain
Version: 1.6.2
Release: alt1

Summary: MP3Gain analyzes and adjusts mp3 files so that they have the same volume.
Group: Sound
License: LGPL
Url: http://mp3gain.sourceforge.net

Source: %name-%version.tar.bz2

BuildRequires: libmpg123-devel

%description
MP3Gain analyzes and adjusts mp3 files so that they have the same volume.

%prep
%setup

%build
make

%install
install -pD -m755 mp3gain %buildroot%_bindir/%name
install -pD -m644 lgpl.txt %buildroot%_docdir/%name-%version/LGPL.txt

%files
%_docdir/%name-%version
%_bindir/%name

%changelog
* Wed Jun 06 2018 Grigory Ustinov <grenka@altlinux.org> 1.6.2-alt1
- Build new version (Closes: #29916).

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.6-alt1.qa2
- NMU: added URL

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.4.6-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Oct 06 2008 Afanasov Dmitry <ender@altlinux.org> 1.4.6-alt1
- initial build

