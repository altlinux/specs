Name: i2myspell
Version: 1.4
Release: alt3

Summary: Ispell to MySpell affix table and dictionary converter
License: BSD
Group: Text tools
Url: http://lingucomponent.openoffice.org/

Packager: Sergey Kurakin <kurakin@altlinux.org>

BuildArch: noarch

Source0: %name
Patch1: i2myspell-1.4-alt-mktemp.patch
Patch2: i2myspell-1.4-alt-cutted_suffixes.patch

%description
i2myspell is a tool to produce myspell/hunspell affix and dictionary
files from ispell hashfile.

%prep
%setup -cT
cat %SOURCE0 | iconv -f=ISO8859-2 -t=UTF-8 > %name
%patch1 -p1
%patch2 -p0

%build

%install
install -d -m755 %buildroot%_bindir
install -p -m755 %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Fri Feb 26 2010 Sergey Kurakin <kurakin@altlinux.org> 1.4-alt3
- fixed conversion of rules with cutted suffixes

* Tue Feb 23 2010 Sergey Kurakin <kurakin@altlinux.org> 1.4-alt2
- noarch architecture

* Fri Feb 19 2010 Sergey Kurakin <kurakin@altlinux.org> 1.4-alt1
- initial build for AltLinux Sisyphus
