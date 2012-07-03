
Summary: The Google Data APIs (GData).
Name: libgoogle-data-mono
Version: 1.4.0.2
Release: alt2
License: Apache
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Url: http://code.google.com/p/google-gdata/
Source: http://google-gdata.googlecode.com/files/%name-%version.tar.gz
Patch1: libgoogle-data-mono-1.4.0.2-alt-pkgconfig.patch
Patch2: libgoogle-data-mono-1.4.0.2-fix-pkgconfig_file.patch

# Automatically added by buildreq on Thu Jun 18 2009
BuildRequires: mono-mcs mono-nunit-devel mono-winforms mono-devel

BuildRequires: rpm-build-mono
BuildRequires: /proc

%description
The Google Data APIs (GData) provide a simple protocol for reading and writing data on the web.

Each of the following Google services provides a Google data API:

    * Base
    * Blogger
    * Calendar
    * Spreadsheets
    * Google Apps Provisioning
    * Code Search
    * Notebook
    * Picasa Web Albums
    * Document Feed
    * Contacts
    * You Tube
    * Google Health 

The GData .NET Client Library provides a library and source code that make it easy to access data through Google Data APIs. 

%package devel
Summary: Develpment files for libgoogle-data-mono
Group: Development/Other
Requires: %name = %version-%release

%description devel
Development files for libgoogle-data-mono

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%__subst 's,libz.so.1.2.3,libz.so.1,g' misc/Google.GData.Client.dll.config

%build
%make PREFIX=%_prefix PKGCONFIGDIR=%_pkgconfigdir

%install
%make_install install DESTDIR=%buildroot PREFIX=%_prefix PKGCONFIGDIR=%_pkgconfigdir
install -m644 misc/Google.GData.Client.dll.config %buildroot%_monogacdir/Google.GData.Client/1.*/

%files
%doc Google* LICENSE-2.0.txt RELEASE_NOTES.HTML
%_monodir/GData-Sharp
%_monogacdir/*

%files devel
%_pkgconfigdir/*

%changelog
* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 1.4.0.2-alt2
- update buildreq

* Thu Jun 18 2009 Alexey Shabalin <shaba@altlinux.ru> 1.4.0.2-alt1
- 1.4.0.2

* Sat Jan 31 2009 Alexey Shabalin <shaba@altlinux.ru> 1.3.1.0-alt1
- Inital build for ALTLinux

