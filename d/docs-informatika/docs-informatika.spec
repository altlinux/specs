Name: docs-informatika
Version: 0.2
Release: alt1

Summary: Practical informatics.
Summary(ru_RU.KOI8-R): Практическая информатика.
License: %gpl2plus
Group: Books/Other
Packager: ALT Docs Team <docs@packages.altlinux.org>
Buildarch: noarch
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace alt-docs-extras-informatika
Provides: alt-docs-extras-informatika = %version
Obsoletes: alt-docs-extras-informatika < %version

Requires: docs-informatika1, docs-informatika2

%description
Free textbook for course "Informatics and informational technologies".

%description -l ru_RU.KOI8-R
Свободные книги курса "Информатика и информационные технологии".

%files

%changelog
* Sun Mar 22 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- initial build for Sisyphus
  + obsoletes alt-docs-extras-informatika package

