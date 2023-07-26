Name: glibc-locales-kv_RU-utf8
Version: 1.0
Release: alt1
Summary: Komi locale for glibc
Group: System/Internationalization
License: LGPL-2.1+
BuildArch: noarch
#https://sourceware.org/bugzilla/show_bug.cgi?id=30605
Source: kv_RU

Requires: glibc-core = %__glibc_version

BuildRequires: glibc-i18ndata

%description
%{summary}.

%prep
%setup -Tc

%build
zcat /usr/share/i18n/charmaps/UTF-8.gz > UTF-8
localedef -f ./UTF-8 -i %{SOURCE0} ./kv_RU.UTF8
find

%install
mkdir -p %buildroot/usr/lib/locale
cp -a kv_RU.UTF8 %buildroot/usr/lib/locale/

%files
/usr/lib/locale/kv_RU.UTF8/

%changelog
* Thu Jul 25 2023 Kirill Izmestev <felixz@altlinux.org> 1.0-alt1
- Initial build.
