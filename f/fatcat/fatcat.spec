Summary: FAT filesystem explore, extract, repair, and forensic tool
Name: fatcat
Version: 1.1.0
Release: alt1
Packager: Igor Vlasenko <viy@altlinux.ru>
License: MIT
Group: File tools
URL: https://github.com/Gregwar/fatcat
VCS: https://github.com/Gregwar/fatcat
BuildRequires: cmake gcc-c++
Source0: %name-%version.tar

%description
fatcat is a tool to explore, extract, repair and forensic FAT filesystem.
 Its features:
     - Get information about FAT filesystem;
     - Explore FAT file system;
     - Read file or extract directories;
     - Retrieve file & directories that are deleted;
     - Backup & restore the FAT tables;
     - Hack the FAT table by writing on it;
     - Hack the entries by changing clusters and file sizes;
     - Perform a search for orphaned files & directories;
     - Compare and merge the FAT tables;
     - Repair unallocated directories &  files;
     - Supports FAT12, FAT16 and FAT32.

%prep
%setup -q
#patch0 -p1

%build
%cmake
%cmake_build

%install
install -D -m 755 BUILD/fatcat %buildroot%_bindir/fatcat
install -D -m 644 man/fatcat.1 %buildroot%_man1dir/fatcat.1

%files
%_bindir/fatcat
%_man1dir/fatcat.1*

%changelog
* Mon Nov 16 2020 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- new version

