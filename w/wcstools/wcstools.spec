# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define  major		1
%define  libname	libwcstools%{major}
%define  develname	libwcstools-devel

Name:		wcstools
Version:	3.9.7
Release:	alt1_1
Summary:	Software utilities to display and manipulate the WCS of a FITS image
License:	GPLv2+
Group:		Sciences/Astronomy
URL:		http://tdc-www.harvard.edu/wcstools
Source0:	http://tdc-www.harvard.edu/software/wcstools/%{name}-%{version}.tar.gz
# Patch from Debian to create shared lib and rename it to avoid
# conflicts with Mark Calabretta's wcslib package.
Patch0:		wcstools-3.9.7-rename-shlib.patch
BuildRequires:	gcc
Source44: import.info

%description
Wcstools is a set of software utilities, written in C, which create,
display and manipulate the world coordinate system of a FITS or IRAF
image, using specific keywords in the image header which relate pixel
position within the image to position on the sky.  Auxiliary programs
search star catalogs and manipulate images.


%package -n %{libname}
Summary:	Wcstools shared library
Group:		Sciences/Astronomy
License:	LGPLv2+

%description -n %{libname}
Shared library necessary to run wcstools and programs based on libwcs.

%package -n %{develname}
Summary:	Libraries, includes, etc. used to develop an application with %{name}
Group:		Sciences/Astronomy
License:	LGPLv2+
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This are the files needed to develop an application using %{name}.

%prep
%setup -q
%patch0 -p1


# Fix wrong FSF address in source headers
# asked upstream by mail to fix this
grep -rl '59 Temple Place, Suite 330, Boston, MA  02111-1307  USA' --include=*.{c,h} | xargs -i@ sed -i 's/59 Temple Place, Suite 330, Boston, MA  02111-1307  USA/51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA./g' @


%build
export CFLAGS="%{optflags}"
export CPPFLAGS="%{optflags}"

# Parallel build fails
make

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_includedir}/libwcs
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0755 bin/* %{buildroot}%{_bindir}

# Rename conflicting binary bug #1450190
# Mailed upstream, no response
# Debian uses the same rename
mv %{buildroot}%{_bindir}/remap %{buildroot}%{_bindir}/wcsremap

cp -a libwcs/*.so* %{buildroot}%{_libdir}
install -p -m 0644 libwcs/*.h %{buildroot}%{_includedir}/libwcs
install -p -m 0644 man/man1/* %{buildroot}%{_mandir}/man1

%files
%doc --no-dereference COPYING
%doc NEWS Readme Programs
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%doc --no-dereference libwcs/COPYING
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%doc libwcs/NEWS
%{_libdir}/*.so
%{_includedir}/libwcs/


%changelog
* Fri Sep 02 2022 Igor Vlasenko <viy@altlinux.org> 3.9.7-alt1_1
- update by mgaimport

* Mon Jun 28 2021 Igor Vlasenko <viy@altlinux.org> 3.9.6-alt1_2
- new version

