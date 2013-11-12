%def_disable docs

Name: jq
Version: 1.3
Release: alt2
Summary: Command-line JSON processor
Group: Development/Other
Source: %name-%version.tar
Patch: %name-%version-%release.patch
URL: http://stedolan.github.io/jq/
License: BSD-style

BuildRequires: flex %{?!_disable_check:valgrind}

%description
%name is a command-line JSON processor.


%prep
%setup -q
%patch -p1


%build
%autoreconf
%configure %{subst_enable docs}
%make_build V=1


%install
%makeinstall_std docdir=%_docdir/%name-%version
ln -sf README.md %buildroot%_docdir/%name-%version/README


%check
%make_build check


%files
%doc %_docdir/%name-%version
%_bindir/*
%_man1dir/*


%changelog
* Tue Nov 12 2013 Led <led@altlinux.ru> 1.3-alt2
- fixed build with new automake

* Fri Oct 11 2013 Led <led@altlinux.ru> 1.3-alt1
- initial build
