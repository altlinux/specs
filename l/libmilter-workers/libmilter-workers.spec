%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define debug_package	%{nil}

%define realversion	8.14.3-1

%define libnamestatic	libmilter-devel-static

Name:		libmilter-workers
Version:	%(echo %realversion | sed 's/-/_/g')
Release:	alt1_12
Summary:	Libmilter and a pool of threads
License:	GPLv1
Group:		Development/C
Url:		http://j-chkmail.ensmp.fr/
Source0:	http://j-chkmail.ensmp.fr/libmilter/%{name}-%{realversion}.tgz
Source1:	http://j-chkmail.ensmp.fr/libmilter/README
Source44: import.info

%description
Under original libmilter each connection generates one thread
on the filter. These threads remain alive during the connection
lifetime. So, one connection equals one thread.

For huge servers, handling many simultaneous connections (say, a
hundred and more), this may be an issue.

Most of the time, these threads are idle waiting for sendmail
commands (which come from remote clients). Tests at some domains
shows that this hold for more than 95 % of the time.

This libmilter version creates a fixed number of threads (workers)
and distribute tasks when it receives commands from sendmail.

%package -n	%{libnamestatic}
Summary:	Libmilter and a pool of threads
Group:		Development/C
Obsoletes:	%{_lib}milterstatic-devel
Provides:	milter-devel = %{version}-%{release}
Provides:	libmilter-devel = %{version}-%{release}

%description -n	%{libnamestatic}
Under original libmilter each connection generates one thread
on the filter. These threads remain alive during the connection
lifetime. So, one connection equals one thread.

For huge servers, handling many simultaneous connections (say, a
hundred and more), this may be an issue.

Most of the time, these threads are idle waiting for sendmail
commands (which come from remote clients). Tests at some domains
shows that this hold for more than 95 % of the time.

This libmilter version creates a fixed number of threads (workers)
and distribute tasks when it receives commands from sendmail.

%prep
%setup -q -n %{name}-%{realversion}
cp -f %{SOURCE1} ./

perl -pi -e "s/-O2/%{optflags}/" devtools/OS/Linux

%build
%make_build

%install
mkdir -p %{buildroot}%{_includedir}/libmilter/
cp include/libmilter/*.h %{buildroot}%{_includedir}/libmilter/

mkdir -p %{buildroot}%{_libdir}
cp obj.`uname -s`.`uname -r`.`uname -m`/libmilter/libmilter.a %{buildroot}%{_libdir}

%files -n %{libnamestatic}
%doc README
%{_includedir}/libmilter/*.h
%{_libdir}/*.a


%changelog
* Sat Aug 28 2021 Igor Vlasenko <viy@altlinux.org> 8.14.3_1-alt1_12
- fixed build with LTO

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 8.14.3_1-alt1_11
- new version

