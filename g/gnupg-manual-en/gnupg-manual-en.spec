%define lang en

Name: gnupg-manual-%lang
Version: 20070416
Release: alt1
Serial: 1

Summary: The GNU Privacy Handbook
Summary(ru_RU.UTF-8): Руководство GNU по обеспечению конфиденциальности
License: FDLv1.1+
Group: Books/Howtos
Url: http://www.gnupg.org/documentation/guides.en.html

Source: gph-svn%version.tar

Provides: gnupg-manual = %version %name = %version
Obsoletes: gnupg-manual <= 1.2.0

BuildArch: noarch

Packager: Sergey Kurakin <kurakin@altlinux.org>

# Automatically added by buildreq on Wed Sep 15 2010 (-bi)
BuildRequires: docbook-utils

%description
The GNU Privacy Handbook
GnuPG is GNU's tool for secure communication and data storage.
It can be used to encrypt data and to create digital signatures.
It includes an advanced key management facility and is compliant
with the proposed OpenPGP Internet standard as described in RFC2440.

%description -l ru_RU.UTF-8
Руководство GNU по обеспечению конфиденциальности
GnuPG - инструмент обеспечения безопасности коммуникаций и хранения
данных. Используется для шифрования данных и создания цифровых
подписей. Включает средства управления ключами и соответствует
предложенному OpenPGP стандарту Internet (RFC2440).

%prep
%setup -c -n %name-%version

%build
cd %lang
#if [ -f signatures.fig -a ! -f signatures.jpg ]; then
#    fig2dev -L jpeg -m 0.7 signatures.fig signatures.jpg
#fi

# remove text of the GNU FDL from the document
# GNU FDL v. 1.1 is a part of common-licenses package
#sed -i "s/&license//g" manual.sgml

# build
db2html -e no-valid manual.sgml
mv signatures.jpg manual/signatures.jpg

# rename index file as index.html with links correction
mv manual/book1.html manual/index.html
sed -i 's/HREF="book1.html"/HREF="index.html"/g' manual/*.html

%install
mkdir -p %buildroot%_defaultdocdir/%name
cp -Rf %lang/manual/* %buildroot%_defaultdocdir/%name

%files
%_defaultdocdir/*

%changelog
* Wed Sep 15 2010 Sergey Kurakin <kurakin@altlinux.org> 1:20070416-alt1
- Update from svn (minor changes)
- License corrected
- Spec cleanup

* Fri May 13 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:1.8-alt2
- Updated BuildRequires

* Mon Feb 02 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1:1.8-alt1
- Version updated up to 1.8
- Source package is splitted into two subpackage - gnupg-manual-en
  and gnupg-manual-ru.
- Updated spec.

* Mon Feb 17 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1:1.2.0-alt1
- Version updated up to 1.2.0.
- Updated and renamed Patch in according to packaging policy.

* Wed Feb 05 2003 Stanislav Ievlev <inger@altlinux.ru> 1:1.1-alt3
- fix changelog

* Mon Feb 03 2003 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.1-alt2
- Updated BuildRequires
- Added Serial, Provides and Obsoletes

* Wed Sep 18 2002 Aleksandr Blokhin <sass@altlinux.ru> 1.1-alt1
- Updated spec.
- Removed unneded description in KOI8 encoding.

* Wed Jun 16 2002 Aleksandr Blokhin <sass@altlinux.ru> 1.1-ipl1
- Manuals updated with new versions.

* Wed Nov 29 2000 Dmitry V. Levin <ldv@fandra.org> 1.0-ipl1
- Initial revision.
