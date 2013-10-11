%def_disable docs

Name: jq
Version: 1.3
Release: alt1
Summary: Command-line JSON processor
Group: Development/Other
Source: %name-%version.tar
URL: http://stedolan.github.io/jq/
License: BSD-style

BuildRequires: flex %{?!_disable_check:valgrind}

%description
%name is a command-line JSON processor.


%prep
%setup -q


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
* Fri Oct 11 2013 Led <led@altlinux.ru> 1.3-alt1
- initial build
