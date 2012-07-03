Summary: Mergemaster for Linux
Name: etc-update
Version: 20020731
Release: alt1
Source0: %name-%version.tar.bz2
Patch0: %name-user.patch
Url: http://www.xs4all.nl/~hanb/software
License: GPL
Group: System/Base
BuildArch: noarch
Requires: setup

%description
After an update with up2date/apt/yum/rpm rpm makes .rpmnew copies of
all files it knows it should not overwrite. Of course you have to look
at all those files and merge any changes. A tedious and much forgotten
job.

On FreeBSD there is mergemaster to do the job. It recently got ported
to OpenBSD and also to Gentoo. Now there is also a Linux version (not
a port) :)

%prep
%setup -q
%patch0 -p1
%__cat << EOF > README.ALT
Following variables may be (re)difined in /e/%{name}rc:

configdirs (default is /etc) - space separated list of dirs, where
*.rpm{save,old,new) files located (along with original files).
Sysadmin may define list of system wide and user-specific dirs.

runtimedir (default is \$TMPDIR) - temporary dir (/tmp if \$TMPDIR is
undefined). Usualy may be omited.

Additionaly, user may specify list of dirs as command-line arguments
(all of them must be writable for him).

EOF

%install
%__mkdir_p %buildroot{%_sysconfdir,%_bindir}
%__install -m 755 %name %buildroot%_bindir
%__install -m 644 %{name}rc %buildroot%_sysconfdir

%files
%config(noreplace) %_sysconfdir/*
%_bindir/*

%doc INSTALL CHANGES README.ALT

%changelog
* Sat Sep 23 2006 Terechkov Evgenii <evg@altlinux.ru> 20020731-alt1
- Build for Sisyphus

* Sat Jul  1 2006 Evgenii Terechkov <evg@altlinux.ru> 20020731-alt0.M24.2
- Support to rpmsave added (merged with user patch)

* Mon Jun 19 2006 Evgenii Terechkov <evg@krastel.ru> 20020731-alt0.M24.1
- Initial build for ALT
- original foo patch merged with my own (rudimentary support for user
  usage)
- move from bash to sh interpreter
- setup is required (for TMPDIR)
