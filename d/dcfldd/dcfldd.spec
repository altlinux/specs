Name: dcfldd
Version: 1.7.1
Release: alt1

Summary: enhanced version of dd for forensics and security
Group: File tools
License: GPL-2.0
Url: https://github.com/resurrecting-open-source-projects/dcfldd

Source: %name-%version.tar
# Source-url: https://github.com/resurrecting-open-source-projects/dcfldd/archive/refs/tags/v%version.tar.gz

%description
dcfldd is an enhanced version of GNU dd with features useful for forensics 
and security. Based on the dd program found in the GNU Coreutils package, 
dcfldd has the following additional features: 
 - Hashing on-the-fly - dcfldd can hash the input data as it is being 
   transferred, helping to ensure data integrity. 
 - Status output - dcfldd can update the user of its progress in terms of the 
   amount of data transferred and how much longer operation will take. 
 - Flexible disk wipes - dcfldd can be used to wipe disks quickly and with a 
   known pattern if desired. 
 - Image/wipe Verify - dcfldd can verify that a target drive is a bit-for-bit 
   match of the specified input file or pattern. 
 - Multiple outputs - dcfldd can output to multiple files or disks at the same 
   time. 
 - Split output - dcfldd can split output to multiple files with more 
   configurability than the split command. 
 - Piped output and logs - dcfldd can send all its log data and output to 
   commands as well as files natively.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*

%changelog
* Sat Sep 11 2021 Anton Midyukov <antohami@altlinux.org> 1.7.1-alt1
- new version (1.7.1) with rpmgs script

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.4.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Mar 14 2008 Maxim Ivanov <redbaron@altlinux.ru> 1.3.4.1-alt1
- Initial build for Sisyphus

