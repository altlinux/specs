%define Name Disc-cover
Name: disc-cover
Version: 1.5.6
Release: alt3
Summary: Makes covers for audio CDs using CDDB info
Summary(uk_UA.CP1251): Виготовлення обкладинок для аудіо-CD з використанням CDDB-інформації
License: %gpl2plus
Group: Sound
Source: http://www.vanhemert.co.uk/files/%name-%version.tar
Patch: %name-cvs-20070116.patch
URL: http://www.vanhemert.co.uk/%name.html
Requires: %_bindir/latex, %_bindir/pdflatex, %_bindir/dvips, %_bindir/convert
BuildArch: noarch
Packager: Led <led@altlinux.org>

BuildRequires(pre): rpm-build-licenses

%description
Provides an easy way to produce covers for audio CDs. It scans audio
CDs and uses information from the CDDB database to build a back and
front cover for the CD. The cover output is in LaTeX, DVI, PDF or
Postscript. This little gadget lets you produce covers without typing
in all the information yourself. An easy way to replace all those lost
covers ;-)


%prep
%setup
%patch -p1


%build
bzip2 --keep --best --force CHANGELOG


%install
install -d -m 0755 %buildroot{%_bindir,%_datadir/%name/templates}
install -m 0755 %name %buildroot%_bindir/
install -m 0644 templates/* %buildroot%_datadir/%name/templates/


%files
%doc AUTHORS CHANGELOG.* TODO docs/english/THANKS
%_bindir/*
%_datadir/%name


%changelog
* Wed Oct 07 2009 Grigory Batalov <bga@altlinux.ru> 1.5.6-alt3
- Replace tetex dependence with latex/dvips binaries.

* Mon Nov 03 2008 Led <led@altlinux.ru> 1.5.6-alt2
- fixed License

* Wed Jun 21 2006 Led <led@altlinux.ru> 1.5.6-alt1
- 1.5.6
- fixed spec
- removed %name-1.5.5-version.patch
- added THANKS to docs

* Mon Jun 19 2006 Led <led@altlinux.ru> 1.5.5-alt1
- 1.5.5
- added %name-1.5.5-version.patch
- added uk_UA Summary

* Thu May 04 2006 Led <led@altlinux.ru> 1.5.4-alt1
- initial build
