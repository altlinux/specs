Name: far2l
Version: 2.0
Release: alt1

Summary: Linux port of FAR v2

Group: File tools
License: GPLv2
Url: https://github.com/elfmz/far2l

# Source-git: https://github.com/elfmz/far2l.git
Source: %name-%version.tar

BuildRequires: gcc-c++ libwxGTK3.1-devel glib2-devel

%description
Linux port of FAR v2
PRE-ALPHA VERSION - currently interesting only for programmers!!!

Better use CodeLite to open and compile this

License: GNU/GPLv2

Used code from projects:
FAR for Windows
Wine
ANSICON

%prep
%setup
%__subst "s|-mcmodel=medium||g" far2l/far2l.mk

%build
%make_build
# FIXME: NEW bad_elf_symbols detected during build on ALT Linux build system
rm -rf Build/Plugins/farftp/

%install
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_libexecdir/%name/
cp -a Build/* %buildroot%_libexecdir/%name/
ln -s ../../%_libexecdir/%name/far2l %buildroot%_bindir/%name

%files
%_bindir/%name
%_libexecdir/%name/

%changelog
* Sat Aug 20 2016 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- initial build for ALT Linux Sisyphus
