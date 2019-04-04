%define        pkgname winrm

Name:          gem-%pkgname
Version:       2.3.1
Release:       alt1
Summary:       Ruby library for Windows Remote Management
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/WinRb/WinRM
# VCS:         https://github.com/WinRb/WinRM.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary.

This is a SOAP library that uses the functionality in Windows Remote Management
(WinRM) to call native object in Windows. This includes, but is not limited to,
running batch scripts, powershell scripts and fetching WMI variables. For more
information on WinRM, please visit Microsoft's WinRM site.

As of version 2.0, this gem retains the WinRM name but all powershell calls use
the more modern Powershell Remoting Protocol (PSRP) for initializing runspace
pools as well as creating and processing powershell pipelines.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%package       -n rwinrm
Summary:       Executable file for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n rwinrm
Executable file for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemdocdir

%files         -n rwinrm
%_bindir/rwinrm

%changelog
* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
