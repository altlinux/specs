%define _unpackaged_files_terminate_build 1
%define  pkgname artifactory-client2

Name:    ruby-%pkgname
Version: 2.8.6
Release: alt2

Summary: A simple, lightweight Ruby client for interacting with the Artifactory API.
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/chef/artifactory-client

BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

Provides: ruby-artifactory-client = %EVR
Conflicts: ruby-artifactory-client


%description
A Ruby client and interface to the Artifactory API. The majority of API endpoints
are only exposed for Artifactory Pro customers! As such, many of the resources and
actions exposed by this gem also require Artifactory Pro.

The Artifactory gem offers a convienent interface for managing various parts of the
Artifactory API. 

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

%files
%doc README* LICENSE
%ruby_sitelibdir/*
%rubygem_specdir/*


%changelog
* Wed Jan 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.8.6-alt2
- Conflict on artifactory-client added

* Mon Jan 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.8.6-alt1
- Initial build for Sisyphus
