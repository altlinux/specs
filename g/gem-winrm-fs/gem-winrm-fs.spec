%define        pkgname winrm-fs

Name:          gem-%pkgname
Version:       1.3.2
Release:       alt1
Summary:       WinRM File Manager 
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/WinRb/winrm-fs
# VCS:         https://github.com/WinRb/winrm-fs.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary.

Files may be copied from the local machine to the winrm endpoint. Individual
files or directories, as well as arrays of files and directories may be
specified.

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%package       -n rwinrmcp
Summary:       Executable file for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n rwinrmcp
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

%files         doc
%ruby_gemdocdir

%files         -n rwinrmcp
%_bindir/rwinrmcp

%changelog
* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.2-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
