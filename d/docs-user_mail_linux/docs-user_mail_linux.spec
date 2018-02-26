# Generated File.
%setup_docs_module user_mail_linux ru

Name: %packagename
Version: 1.3.1
Release: alt7

Summary: Mail System in Linux
Summary(ru_RU.KOI8-R): Настройка почтовой системы в Linux
License: %fdl
Url: http://gir.nongnu.org/people/daa/texts/linuxmail.html
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-user_mail_linux-alenitchev
Provides: docs-user_mail_linux-alenitchev
Obsoletes: docs-user_mail_linux-alenitchev

Source: %name-%version.tar

%description
Tuning workstation for work with e-mail.

%description -l ru_RU.KOI8-R
Из данного документа вы узнаете о том, как организована работа с почтой в Linux. Также вы научитесь самостоятельно настраивать почтовую систему и работать с описанными инструментами.

%prep
%setup

%build
%docs_module_build "DocBook/XML" "linuxmail.xml"

%install
%docs_module_install

%files
%docs_module_files

%changelog
* Sun Jun 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 1.3.1-alt7
- replaces docs-user_mail_linux-alenitchev
  + added Provides/Obsoletes

* Mon Apr 07 2008 Artem Zolochevskiy <azol@altlinux.ru> 1.3.1-alt6
- initial build for Sisyphus
  + based on docs-user_mail_linux-alenitchev package

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.1-alt5.1.1.1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 1.3.1-alt5.1.1.1
- Auto rebuild with new version.

* Thu Sep 29 2005 Kirill Maslinsky <kirill@altlinux.ru> 1.3.1-alt5.1.1
- Auto rebuild with new version.

* Wed Sep 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 1.3.1-alt5.1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 1.3.1-alt5
- rebuilt with rpm-build-docs-0.4.2-alt3

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 1.3.1-alt4
- rebuilt with rpm-build-docs-0.4.2-alt2

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 1.3.1-alt3
- Requires bugfix;

* Mon Jun 06 2005 Alexey Gladkov <legion@altlinux.ru> 1.3.1-alt2
- rebuild with new rpm-build-docs.

* Thu Apr 28 2005 Kirill Maslinsky <kirill@altlinux.ru> 1.3.1-alt1
- new version in DocBook/XML format

* Mon Apr 11 2005 Kirill Maslinsky <kirill@altlinux.ru> 1.3-alt1
- initial build

