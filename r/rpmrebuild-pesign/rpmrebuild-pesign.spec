Name: rpmrebuild-pesign
Version: 0.1.1
Release: alt1

Summary: Signer for packages containing PE format files
License: GPL
Group: Development/Other
BuildArch: noarch

Source: %name-%version.tar

Requires: rpmrebuild
Requires: pesign

%description
%{summary}.

%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/rpmrebuild/plugins/
install -m644 pesign.plug %buildroot%_libexecdir/rpmrebuild/plugins/
install -m755 pesign.sh %buildroot%_libexecdir/rpmrebuild/plugins/

%files
%_libexecdir/rpmrebuild/plugins/pesign.*

%changelog
* Wed Dec 11 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.1-alt1
- Fixed work with pesign-client.

* Thu Dec 05 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt1
- Initial build.

