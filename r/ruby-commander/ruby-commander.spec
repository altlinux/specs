%define orig_name commander

Summary: The complete solution for Ruby command-line executable
Name: ruby-%orig_name
Version: 4.1.2
Release: alt1
Group: Development/Ruby
License: MIT
Packager: Evgeny Sinelnikov <sin@altlinux.ru>
URL: http://visionmedia.github.com/commander
Source0: %orig_name-%version.tar
Patch0: %orig_name-%version-%release.patch

BuildArch: noarch

BuildRequires: rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
The complete solution for Ruby command-line executable


%prep
%setup -q -n %orig_name-%version
%patch -p1
%update_setup_rb

%build
%ruby_config

%install
%ruby_install

%files
%doc Manifest History.rdoc README.rdoc
%_bindir/commander
%ruby_sitelibdir/*


%changelog
* Wed Aug 01 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.2-alt1
- Initial build for Sisyphus
