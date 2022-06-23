%define _unpackaged_files_terminate_build 1

Name: paxmirabilis
Version: 20201030
Release: alt1
Summary: pax - the POSIX standard archive tool for cpio and tar formats

License: BSD
Group: Archiving/Backup
URL: https://www.mirbsd.org/pax.htm
VCS: git+https://github.com/MirBSD/mircpio.git

Source: %name-%version.tar

%description
'pax' (Portable Archive Interchange) is the POSIX standard archive tool.
It supports the two most common forms of standard Unix archive (backup) files -
CPIO and TAR.

This is git version of pax from MirBSD.

%prep
%setup

# license
sed -n '5,36p' pax.h > LICENSE # create file
sed -i '1,32s/^.\{,3\}//' LICENSE # erase C comments

%build
mkdir -p build
cd build
sh ../Build.sh -r -tpax

%install
%define exename paxmirabilis
# executables
install -D -m755 build/pax %buildroot%_bindir/%exename
# should be alternatives
#ln -s %exename %buildroot/usr/bin/pax
#ln -s %exename %buildroot/usr/bin/paxcpio
#ln -s %exename %buildroot/usr/bin/paxtar

# man pages
install -D -m644 build/mans/pax.1 -t %buildroot%_man1dir/%exename.1
# should be alternatives
#ln -s %exename.1 %buildroot%_man1dir/pax.1


%files
%doc LICENSE
%_bindir/*
%_man1dir/*

%changelog
* Thu Jun 23 2022 Igor Vlasenko <viy@altlinux.org> 20201030-alt1
- Inital release
