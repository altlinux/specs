%define cldrdir %_datadir/unicode/cldr

Name: cldr
Version: 40
Release: alt1

Summary: Unicode Common Locale Data Repository
Group: Development/Other
License: Unicode-TOU

Url: http://cldr.unicode.org/index

%define oversion %(echo "%version" | sed -e "s|\\\\.|-|g")
# Source-url: https://github.com/unicode-org/cldr/archive/release-%oversion.tar.gz
Source: %name-%version.tar

BuildArch: noarch

AutoReq: no

Requires: %name-core = %version-%release
Requires: %name-exemplars = %version-%release
Requires: %name-keyboards = %version-%release
Requires: %name-seed = %version-%release
Requires: cldr-emoji-annotation

%description
The Unicode CLDR provides key building blocks for software to support the world's languages,
with the largest and most extensive standard repository of locale data available.
This data is used by a wide spectrum of companies for their software internationalization and localization,
adapting software to the conventions of different languages for such common software tasks.

%package dirs
Summary: Common directories for CLDR
Group: Development/Other

%description dirs
This package contains common directories for CLDR.

%package common
Summary: Core files (common directory) from CLDR
Group: Development/Other
Requires: %name-dirs = %version-%release
Provides: %name-core = %version-%release

%description common
The Unicode CLDR provides key building blocks for software to support the world's languages,
with the largest and most extensive standard repository of locale data available.
This data is used by a wide spectrum of companies for their software internationalization and localization,
adapting software to the conventions of different languages for such common software tasks.

This package contains core (common) files from CLDR.

%package exemplars
Summary: Exemplars files from CLDR
Group: Development/Other
Requires: %name-dirs = %version-%release

%description exemplars
The Unicode CLDR provides key building blocks for software to support the world's languages,
with the largest and most extensive standard repository of locale data available.
This data is used by a wide spectrum of companies for their software internationalization and localization,
adapting software to the conventions of different languages for such common software tasks.

This package contains exemplars files from CLDR.

%package keyboards
Summary: Keyboards files from CLDR
Group: Development/Other
Requires: %name-dirs = %version-%release

%description keyboards
The Unicode CLDR provides key building blocks for software to support the world's languages,
with the largest and most extensive standard repository of locale data available.
This data is used by a wide spectrum of companies for their software internationalization and localization,
adapting software to the conventions of different languages for such common software tasks.

This package contains keyboards files from CLDR.

%package seed
Summary: Seed files from CLDR
Group: Development/Other
Requires: %name-dirs = %version-%release

%description seed
The Unicode CLDR provides key building blocks for software to support the world's languages,
with the largest and most extensive standard repository of locale data available.
This data is used by a wide spectrum of companies for their software internationalization and localization,
adapting software to the conventions of different languages for such common software tasks.

This package contains seed files from CLDR.

%package docs
Summary: Documentation for CLDR
Group: Development/Other

%description docs
The Unicode CLDR provides key building blocks for software to support the world's languages,
with the largest and most extensive standard repository of locale data available.
This data is used by a wide spectrum of companies for their software internationalization and localization,
adapting software to the conventions of different languages for such common software tasks.

This package contains documentation for CLDR.


%prep
%setup

%build

%install
mkdir -p %buildroot%cldrdir/common/
cp -a common/* %buildroot%cldrdir/common/
# packed from other source to cldr-emoji-annotation
rm -rf %buildroot%cldrdir/common/{annotations,annotationsDerived}/
cp -a {exemplars,keyboards,seed} %buildroot%cldrdir/
mkdir -p %buildroot%_docdir/cldr/
cp -a specs/* %buildroot%_docdir/cldr/


%files dirs
%doc README.md readme.html unicode-license.txt
%dir %_datadir/unicode/
%dir %cldrdir/

%files common
%dir %cldrdir/common/
%cldrdir/common/*

%files exemplars
%cldrdir/exemplars/

%files keyboards
%cldrdir/keyboards/

%files seed
%dir %cldrdir/seed/
%cldrdir/seed/*

%files docs
%_docdir/cldr/

%files

%changelog
* Sun Mar 20 2022 Vitaly Lipatov <lav@altlinux.ru> 40-alt1
- new version 40 (with rpmrb script)

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 39-alt1
- new version 39 (with rpmrb script)

* Mon Dec 28 2020 Vitaly Lipatov <lav@altlinux.ru> 38.1-alt1
- new version 38.1 (with rpmrb script)
- move requires from description section (thanks, mike@!)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 36-alt1
- initial build for Sisyphus
