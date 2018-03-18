# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 2
%define libname libview%{major}
%define develname libview-devel

Summary: VMware's Incredibly Exciting Widgets
Name: libview
Version: 0.6.6
Release: alt1_9
Source0: http://prdownloads.sourceforge.net/view/%{name}-%{version}.tar.bz2
Patch:	 libview-0.6.2-fix-pkgconfig.patch
Patch1:  libview-0.6.6-automake-1.13.patch
License: MIT
Group: System/Libraries
Url: http://view.sourceforge.net/
BuildRequires: libgtkmm2-devel
Source44: import.info

%description
libview is VMware's Incredibly Exciting Widgets, a useful collection
of GTK+ widgets used within VMware products, free for everybody's use.

%package -n %libname
Group: System/Libraries
Summary: VMware's Incredibly Exciting Widgets

%description -n %libname
libview is VMware's Incredibly Exciting Widgets, a useful collection
of GTK+ widgets used within VMware products, free for everybody's use.

%package -n %develname
Group: Development/C++
Summary: VMware's Incredibly Exciting Widgets
Requires: %libname = %version-%release
Provides: libview-devel = %version-%release

%description -n %develname
libview is VMware's Incredibly Exciting Widgets, a useful collection
of GTK+ widgets used within VMware products, free for everybody's use.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
#gw 0.6.6: wrong libtool version
autoreconf -fi
CXXFLAGS="%{optflags} -std=gnu++11" \
%configure --enable-deprecated --disable-static
%make

%install
%makeinstall_std

rm -f %{buildroot}%_libdir/*.la

%files -n %libname
%doc AUTHORS README NEWS
%_libdir/libview.so.%{major}*

%files -n %develname
%doc ChangeLog
%_libdir/libview.so
%_libdir/pkgconfig/libview.pc
%_includedir/libview


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt1_9
- new version

