Summary: Tex2im is a simple tool that converts LaTeX formulas into high resolution pixmap graphics.
Summary(be_BY.UTF-8): Просты інструмэнт які дазваляе пераўтвараць формулы LaTeX у высокаякасныя графічныя відарысы.
Name:       tex2im
Version:    1.8
Release:    alt3
License:    GPL
Group:      Text tools
Url:   http://www.nought.de/tex2im.php

Source:     %name-%version.tar.gz

%description
Tex2im is a simple tool that converts LaTeX formulas into high resolution
pixmap graphics for inclusion in text processors or presentations.

%description -l be_BY.UTF-8
Просты інструмэнт які дазваляе пераўтвараць формулы LaTeX у высокаякасныя графічныя відарысы
для выкарыстаньня тэкставымі працэсарамі й прэзэнтацыямі.

%prep
%setup -q -n %name-%version

%install
%__mkdir_p %buildroot%_bindir
cp tex2im %buildroot%_bindir/

%files
%doc {README,examples}
%_bindir/tex2im

%changelog
* Tue Oct 06 2009 Grigory Batalov <bga@altlinux.ru> 1.8-alt3
- Remove hardcoded dependencies due to successful robot.

* Thu Aug 04 2005 Vital Khilko <vk@altlinux.ru> 1.8-alt2
- fixed #7505

* Wed Jun 15 2005 Vital Khilko <vk@altlinux.ru> 1.8-alt1
- initial build for ALT Linux Sisyphus 

