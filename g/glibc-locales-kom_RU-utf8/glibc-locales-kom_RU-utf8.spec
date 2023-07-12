Name: glibc-locales-kom_RU-utf8
Version: 1.0
Release: alt1
Summary: Komi locale for glibc
Group: System/Internationalization
License: LGPL-2.1+
BuildArch: noarch
#https://sourceware.org/bugzilla/show_bug.cgi?id=30605
Source: kom_RU

Requires: glibc-core = %__glibc_version

BuildRequires: glibc-i18ndata

%description
%{summary}.

%prep
%setup -Tc

%build
zcat /usr/share/i18n/charmaps/UTF-8.gz > UTF-8
localedef -f ./UTF-8 -i %{SOURCE0} ./kom_RU.UTF-8
find

%install
mkdir -p %buildroot/usr/lib/locale
cp -a kom_RU.UTF-8 %buildroot/usr/lib/locale/

%files
/usr/lib/locale/kom_RU.UTF-8/

%changelog
* Wed Jul 12 2023 Kirill Izmestev <felixz@altlinux.org> 1.0-alt1
- Initial build.
