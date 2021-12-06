%define oname liblarch

Name: python3-module-%oname
Version: 3.1.0
Release: alt1

Summary: A Python library to easily handle complex data structures, with a GTK binding

License: LGPL-3.0-only
Group: Development/Python
Url: https://github.com/getting-things-gnome/liblarch

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
Liblarch is a python library built to easily handle data structure
such are lists, trees and acyclic graphs (tree where nodes can have
multiple parents). There's also a liblarch-gtk binding that will allow
you to use your data structure into a Gtk.Treeview.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{oname}_gtk/
%python3_sitelibdir/*.egg-*

%changelog
* Mon Dec 06 2021 Vladimir Didenko <cow@altlinux.org> 3.1.0-alt1
- new version

* Thu Jul 09 2020 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt1
- initial build for Sisyphus
