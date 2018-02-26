%define _altdata_dir %_datadir/alterator

Name: alterator-bacula-client
Version: 0.1
Release: alt1

Packager: Alexandra Panyukova <mex3@altlinux.ru>

BuildArch: noarch

Source:%name-%version.tar

Summary: alterator module for client bacula administration
License: GPL
Group: System/Configuration/Other

Conflicts: alterator-fbi < 2.8-alt1
Conflicts: alterator-lookout < 1.2-alt1
Requires: alterator >= 3.1-alt6
Requires: alterator-sh-functions >= 0.6-alt3
Requires: alterator-bacula-functions

BuildPreReq: alterator >= 3.3-alt5

# Automatically added by buildreq on Mon Jul 11 2005 (-bi)
BuildRequires: alterator

%description
alterator module for client bacula administration

%prep
%setup -q

%build
%make_build libdir=%_libdir

%install
%makeinstall

%files
%_altdata_dir/ui/*/
%_altdata_dir/applications/*
%_alterator_backend3dir/*

%changelog
* Mon Feb 21 2010 Alexandra Panyukova <mex3@altlinux.ru> 0.1-alt1
- Initial release

