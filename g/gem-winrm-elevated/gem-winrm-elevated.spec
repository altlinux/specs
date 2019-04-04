%define        pkgname winrm-elevated

Name:          gem-%pkgname
Version:       1.1.1
Release:       alt1
Summary:       Runs PowerShell commands as elevated over Windows Remote Management (WinRM) via a scheduled task 
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/WinRb/winrm-elevated
# VCS:         https://github.com/WinRb/winrm-elevated.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary.

This gem allows you to break out of the magical WinRM constraints thus allowing
to reach out to network shares and even install Windows updates, .NET, SQL
Server etc.

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


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

%changelog
* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
