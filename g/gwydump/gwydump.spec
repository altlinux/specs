Name: gwydump
Url: http://gwyddion.net/gwydump.php
Version: 2.0
Release: alt1
License: GPL
Packager: Boris Savelev <boris@altlinux.org>

Source: %name-%version.tar.bz2
Group: Sciences/Other
Summary: gwydump dumps the structure and possibly contents of .gwy file

# Automatically added by buildreq on Sat Jul 04 2009
BuildRequires: glib2-devel

%description
gwydump dumps the structure and possibly contents of .gwy files in textual form
and it can also extract raw data components from them. 
It is very useful for getting acquainted with the file strcuture, 
obtaining overview of file contents from command line, debugging problems or writing a program to read .gwy files.

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc README
%_bindir/%name

%changelog
* Sat Jul 04 2009 Boris Savelev <boris@altlinux.org> 2.0-alt1
- initial build for Sisyphus

