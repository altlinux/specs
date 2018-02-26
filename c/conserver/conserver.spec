%define unstable 0

Name:    conserver
Version: 8.1.16
Release: alt1.1

Summary:  Serial console server daemon/client
License:  %bsd
Packager: Andriy Stepanov <stanv@altlinux.ru>

Group:   System/Servers
URL:     http://www.conserver.com/
Source:  %{name}-%{version}.tar
Source1: conserver.init

Patch:  certificate-auth.patch

BuildRequires: openssl-devel
BuildRequires: rpm-build-licenses

%description
Conserver is an application that allows multiple users to watch a
serial console at the same time.  It can log the data, allows users to
take write-access of a console (one at a time), and has a variety of
bells and whistles to accentuate that basic functionality.

%prep
%setup -q
%patch -p1

%build

%if %unstable
%define optflags_debug -g
%define _optlevel 0
%add_optflags %optflags_debug
%def_enable debug
export stripprog=""
export stripcmd=""
%endif

%add_optflags %optflags_debug %optflags_shared
export CFLAGS="%optflags"

# define the name of the machine on which the main conserver
# daemon will be running if you don't want to use the default
# hostname (console)
%define master console

%configure --with-master=%{master} \
          %{subst_enable debug} \
           --with-openssl
#           --with-pam \
#           --with-libwrap

%define __nprocs 1
%make_build

%install
%if %unstable
%set_strip_method none
%endif
%makeinstall

# put commented copies of the sample configure files in the
# system configuration directory
install -d -pm 755 %{buildroot}/%{_sysconfdir}

%{__sed} -e 's/^/#/' \
  < conserver.cf/conserver.cf \
  > %{buildroot}/%{_sysconfdir}/conserver.cf

%{__sed} -e 's/^/#/' \
  < conserver.cf/conserver.passwd \
  > %{buildroot}/%{_sysconfdir}/conserver.passwd

# Init scrips.
install -d -pm 755 %{buildroot}%{_initdir}
install -D -pm 755 %{S:1} %{buildroot}%{_initdir}/conserver

%post
%post_service conserver

# make sure /etc/services has a conserver entry
if ! egrep conserver /etc/services > /dev/null 2>&1 ; then
  echo "console		782/tcp		conserver" >> /etc/services
fi

%preun
%preun_service conserver

%files
%{_initdir}/*
%{_bindir}/console
%{_sbindir}/conserver
%{_libdir}/conserver/convert
%doc CHANGES FAQ INSTALL README conserver.cf
%doc %_mandir/*/*
%config(noreplace) %{_sysconfdir}/conserver.cf
%config(noreplace) %{_sysconfdir}/conserver.passwd

%changelog
* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 8.1.16-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue Nov 17 2009 Andriy Stepanov <stanv@altlinux.ru> 8.1.16-alt1
- ALT: initial build

