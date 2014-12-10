Name: libass4
Version: 0.10.1
Release: alt2
Summary: Portable library for SSA/ASS subtitles rendering

Group: System/Legacy libraries
License: BSD
Url: http://code.google.com/p/libass/
Source: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: libpng-devel libenca-devel fontconfig-devel libfreetype-devel
BuildRequires: libfribidi-devel libharfbuzz-devel

%description
libass is portable library for SSA/ASS subtitles rendering.

%package -n libass
Summary: Portable library for SSA/ASS subtitles rendering
Group: System/Legacy libraries

%description -n libass
libass is portable library for SSA/ASS subtitles rendering.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files -n libass
%doc COPYING Changelog
%_libdir/*.so.*

%changelog
* Wed Dec 10 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.1-alt2
- rebuilt as shared library only

* Fri Sep 20 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.1-alt1
- 0.10.1 release

* Tue Aug 30 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.13-alt1
- 0.9.13 release

* Sun Jun 12 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.12-alt1
- 0.9.12 release

* Sun Nov 07 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.11-alt2
- rebuilt with set-versioned rpm

* Wed Aug 18 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.11-alt1
- 0.9.11 release

* Wed Mar 03 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.9-alt1
- 0.9.9 release

* Sun Dec 27 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.8-alt2
- unwanted free() in ass_read_memory fixed

* Sat Nov 14 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.8-alt1
- 0.9.8 release

* Sat Nov 14 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.7-alt1
- 0.9.7 release

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.5-alt1
- Initial build for ALT Linux.

