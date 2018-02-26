Name: gnupg-manual-ru
Version: 20070216
Release: alt1
Serial: 1

Summary: Russian translation of The GNU Privacy Handbook 
Summary(ru_RU.UTF-8): Руководство GNU по обеспечению конфиденциальности на русском языке
License: FDLv1.1+
Group: Books/Howtos
Url: http://gnupg.trinitum.org/

Source: gph-ru.tar

Provides: gnupg-manual-ru = %version
Obsoletes: gnupg-manual <= 1.2.0

BuildArch: noarch

Packager: Sergey Kurakin <kurakin@altlinux.org>

BuildRequires: xmlto

%description
The GNU Privacy Handbook
Russian translation by Pavel Shaydo

GnuPG is GNU's tool for secure communication and data storage.
It can be used to encrypt data and to create digital signatures.
It includes an advanced key management facility and is compliant
with the proposed OpenPGP Internet standard as described in RFC2440.

%description -l ru_RU.UTF-8
Руководство GNU по обеспечению конфиденциальности
в переводе на русский Павла Шайдо

GnuPG - инструмент обеспечения безопасности коммуникаций и хранения
данных. Используется для шифрования данных и создания цифровых
подписей. Включает средства управления ключами и соответствует
предложенному OpenPGP стандарту Internet (RFC2440).


%prep
%setup -c -n %name-%version

%build
#if [ -f signatures.fig -a ! -f signatures.jpg ]; then
#    fig2dev -L jpeg -m 0.7 signatures.fig signatures.jpg
#fi
LC_ALL=ru_RU.UTF-8 xmlto --skip-validation -o manual html manual.xml
mv signatures.png C2from_n.png manual/

%install
mkdir -p %buildroot%_defaultdocdir/%name
cp -Rf manual/* %buildroot%_defaultdocdir/%name

%files
%_defaultdocdir/*

%changelog
* Thu Sep 16 2010 Sergey Kurakin <kurakin@altlinux.org> 1:20070216-alt1
- Update (minor changes)
- License corrected
- Url updated
- Spec cleanup


* Fri May 13 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1:1.7-alt2
- Updated BuildRequires

* Mon Feb 02 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1:1.7-alt1
- Version updated up to 1.7
- Source package is splitted into two subpackage - gnupg-manual-en
  and gnupg-manual-ru.
- Updated spec.
- Updated patch.

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
