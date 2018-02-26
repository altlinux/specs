Name: installer-sdk
Version: 0.1.1
Release: alt1

Summary: Installer feature simple development kit ;)
License: GPL
Group: Development/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
AutoReq: no

%define featurist init-installer-feature

%description
This package provides a simple installer feature template
and a script to rename/substitute the stub with the name
you chose for the module to be written; it's not any kind
of "wizard" at all but should spare some time on doing 
redundant work.

Any suggestions on template and processing as well as 
other contributions are of course welcome!

Recommended packages: git-core, tree

%prep
%setup

%install
sed -i 's,@TOOLNAME@,%name,g' %featurist
sed -i 's,@TEMPLATE@,%_datadir/%name/template,g' %featurist
install -pD -m755 %featurist %buildroot%_bindir/%featurist
install -d %buildroot%_datadir/%name
cp -a template %buildroot%_datadir/%name/

%files
%_bindir/*
%_datadir/%name/

# TODO:
# - add help for quite cryptic template functionality :)
# - split quite common templating "engine" to reuse within
#   both installer-sdk and alterator-sdk

%changelog
* Tue Aug 12 2008 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- updated Url: in both package and template specs

* Thu Apr 10 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- removed extra copies of sample script
- moved sample up one dir (should still be removed if unneeded
  as well as extra dirs)

* Tue Apr 08 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on alterator-sdk 0.1-alt1)
- AutoReq: no (we don't want to depend on installer-stage2)
