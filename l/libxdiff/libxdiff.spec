# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define	major 0
%define	libname libxdiff%{major}
%define develname libxdiff-devel

Name:		libxdiff
Version:	0.23
Release:	alt1_7
Summary:	Create diffs/patches for text/binary files
License:	LGPLv2.1+
Group:		System/Libraries
URL:		http://www.xmailserver.org/xdiff-lib.html
Source0:	http://www.xmailserver.org/%{name}-%{version}.tar.gz
Patch0:		am-fixes.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Source44: import.info

%description
The LibXDiff library implements basic and yet complete functionalities
to create file differences/patches to both binary and text files. It
uses memory files as file abstraction to achieve both performance and
portability. For binary files, it implements (with some modification)
the algorithm described in "File System Support for Delta Compression"
by Joshua P. MacDonald. For text files, it follows directives described
in "An O(ND) Difference Algorithm and Its Variations" by Eugene W.
Myers. Memory files used by the library are basically a collection of
buffers that store the file content.


%package -n	%{libname}
Summary:	Shared libxdiff library
Group:		System/Libraries

%description -n	%{libname}
The LibXDiff library implements basic and yet complete functionalities
to create file differences/patches to both binary and text files. It
uses memory files as file abstraction to achieve both performance and
portability. For binary files, it implements (with some modification)
the algorithm described in "File System Support for Delta Compression"
by Joshua P. MacDonald. For text files, it follows directives described
in "An O(ND) Difference Algorithm and Its Variations" by Eugene W.
Myers. Memory files used by the library are basically a collection of
buffers that store the file content


%package -n	%{develname}
Summary:	Header files for libxdiff library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
The LibXDiff library implements basic and yet complete functionalities to
create file differences/patches to both binary and text files. It uses memory
files as file abstraction to achieve both performance and portability. For
binary files, it implements (with some modification) the algorithm described in
"File System Support for Delta Compression" by Joshua P. MacDonald. For text
files, it follows directives described in "An O(ND) Difference Algorithm and
Its Variations" by Eugene W. Myers. Memory files used by the library are
basically a collection of buffers that store the file content.

Header files for libxdiff library.


%prep
%setup -q
%patch0 -p0

%build
%serverbuild
autoreconf -fis

%configure \
    --with-pic

%make

%install
%makeinstall_std

#don't ship static libraries
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%{_includedir}/*.h
%{_libdir}/*.so
%{_mandir}/man?/*


%changelog
* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_7
- new version

