# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit 8d91e8a2009ff9196454fea1362627fd1f921196
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global devel_version_num 2020.0.0
%global commitnum 338
%global commitdate 20190804
%global vcs_version 2020.0.0-alpha1-%{commitnum}-%{shortcommit}

%define rel 2

Name:           ksh
Epoch:          1
Version:        %{devel_version_num}.%{commitnum}.git%{shortcommit}
Release:        alt2_0.%{rel}
Summary:        The Original ATT Korn Shell
Group:          Shells
License:        EPL
URL:            http://www.kornshell.com/
Source0:        https://github.com/att/ast/archive/%{commit}/%{name}-%{version}.tar.gz
Source1:        kshcomp.conf
Source2:        kshrc.rhs
Source3:        dotkshrc

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  glibc-devel glibc-devel-static
# This package is require by test cases
# It should be enabled when we start running test cases in package builds
# BuildRequires:  glibc-langpack-zh
BuildRequires:  ed
Conflicts:      pdksh
Requires(post): grep, coreutils, systemd-utils
Requires(postun): sed

Provides:       /bin/ksh
Source44: import.info

%description
KSH-93 is the most recent version of the KornShell by David Korn of
AT&T Bell Laboratories.
KornShell is a shell programming language, which is upward compatible
with "sh" (the Bourne Shell).

%prep
%setup -q -n ast-%{commit}


%build
%meson -Dbuild-api-tests=false -Dfallback-version-number=%{vcs_version}
%meson_build

%install
%meson_install

install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/binfmt.d/kshcomp.conf
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/kshrc
install -p -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/skel/.kshrc

ln -s %{_bindir}/ksh %{buildroot}%{_bindir}/rksh

%post
for s in /bin/ksh /bin/rksh /usr/bin/ksh /usr/bin/rksh 
do
  if [ ! -f /etc/shells ]; then
        echo "$s" > /etc/shells
  else
        if ! grep -q '^'"$s"'$' /etc/shells ; then
                echo "$s" >> /etc/shells
        fi
  fi
done

/bin/systemctl try-restart systemd-binfmt.service >/dev/null 2>&1 || :

%postun
for s in /bin/ksh /bin/rksh /usr/bin/ksh /usr/bin/rksh 
do
  if [ ! -f $s ]; then
     sed -i '\|^'"$s"'$|d' /etc/shells
  fi
done

%verifyscript
echo -n "Looking for ksh in /etc/shells... "
if ! grep '^/bin/ksh$' /etc/shells > /dev/null; then
    echo "missing"
    echo "ksh missing from /etc/shells" >&2
else
    echo "found"
fi

%files
%doc README.md src/cmd/ksh93/COMPATIBILITY src/cmd/ksh93/RELEASE src/cmd/ksh93/TYPES
%doc --no-dereference LICENSE
%{_bindir}/ksh
%{_bindir}/rksh
%{_bindir}/shcomp
%{_mandir}/man1/ksh.1*
%config(noreplace) %{_sysconfdir}/skel/.kshrc
%config(noreplace) %{_sysconfdir}/kshrc
%config(noreplace) %{_sysconfdir}/binfmt.d/kshcomp.conf


%changelog
* Mon Sep 18 2023 Ilya Mashkin <oddity@altlinux.ru> 1:2020.0.0.338.git8d91e8a-alt2_0.2
- Build for Sisyphus, needed by NsCDE

* Tue Mar 10 2020 Igor Vlasenko <viy@altlinux.ru> 1:2020.0.0.338.git8d91e8a-alt1_0.2
- update by mgaimport

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 1:2020.0.0.338.git8d91e8a-alt1_0.1
- new version

