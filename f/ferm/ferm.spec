# SPEC file for ferm
#

Name: ferm
Version: 2.7
Release: alt1

Summary: iptables frontend For Easy Rule Making

License: %gpl2only
Group: Security/Networking
URL: http://ferm.foo-projects.org/
#URL: https://github.com/MaxKellermann/ferm

Packager: Nikolay A. Fetisov <naf@altlinux.org>
BuildArch: noarch

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Patch1:  %name-2.6-alt-exclude_rpm_files.patch

Source1: ferm.conf
Source2: %name.service
Source3: %name.init
Source4: %name.sysconfig

BuildRequires(pre): rpm-build-licenses

Requires: iptables

# Automatically added by buildreq on Tue Aug 11 2020
# optimized out: perl perl-Encode perl-HTML-Parser perl-Pod-Escapes perl-Pod-Simple perl-parent perl-podlators python-modules python2-base python3 python3-base python3-dev ruby ruby-stdlibs sh4
BuildRequires: perl-Pod-Usage perl-devel

%description
ferm, pronounced "firm", stands for "For Easy Rule Making",
is a frontend for iptables. It reads the rules from
a structured configuration file and calls iptables(8)
to insert them into the running kernel.

ferm's goal is to make firewall rules easy to write and easy
to read. It tries to reduce the tedious task of writing down
rules, thus enabling the firewall administrator to spend
more time on developing good rules than the proper
implementation of the rule.

To achieve this, ferm uses a simple but powerful configuration
language, which allows variables, functions, arrays, blocks.
It also allows you to include other files, allowing you to
create libraries of commonly used structures and functions.


%prep
%setup
%patch0 -p1

%patch1

ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/LICENSE) LICENSE

%build
%make
%make test

%install
%make_install install PREFIX=%buildroot%_usr

# Clean unused installed files
rm -f -- COPYING && mv -- LICENSE COPYING
rm -rf -- %buildroot%_defaultdocdir/%name
rm -rf -- %buildroot/usr/lib/systemd

# Install sample configuration file
mkdir -p -- %buildroot%_sysconfdir/ferm/ferm.d/
install -m 0644 %SOURCE1 %buildroot%_sysconfdir/ferm/ferm.conf

# Install systemd unit file, init script:
install -pD -m0644 -- %SOURCE2  %buildroot%_unitdir/%name.service
install -pD -m0755 -- %SOURCE3  %buildroot%_initdir/%name
install -pD -m0640 -- %SOURCE4  %buildroot%_sysconfdir/sysconfig/%name


%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS NEWS README.rst TODO
%doc --no-dereference COPYING
%doc examples/

%_sbindir/%name
%_sbindir/import-ferm
%_man1dir/%{name}*
%_man1dir/import-ferm*

%dir %attr(0700,root,root) %_sysconfdir/ferm/
%dir %attr(0755,root,root) %_sysconfdir/ferm/ferm.d/
%config(noreplace) %_sysconfdir/ferm/ferm.conf

%_unitdir/%name.service
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name


%changelog
* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 2.7-alt1
- New version:
  * support for the nfacct netfilter module
  * support "--random-fully" for the MASQUERADE netfilter module

* Wed Jul 14 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.6-alt2
- Skip rpmnew/rpmsave files in the @include directive

* Wed Jun 23 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.6-alt1
- Initial build for ALT Linux Sisyphus
