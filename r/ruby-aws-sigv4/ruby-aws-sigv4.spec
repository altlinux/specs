Name:    ruby-aws-sigv4
Version: 1.0.2
Release: alt1

Summary: AWS Signature Version 4 library
Group:   Development/Ruby
License: Apache2
URL:     http://github.com/aws/aws-sdk-ruby
#VCS:    https://github.com/aws/aws-sdk-ruby/tree/master/gems/aws-sigv4

BuildArch: noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

Source: aws-sigv4-%version.tar

%description
Amazon Web Services Signature Version 4 signing ligrary. Generates sigv4
signature for HTTP requests.

%package doc
Summary:   Documentation for %name
Group:     Development/Documentation
Requires:  %name = %version-%release
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -n aws-sigv4-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%check
%ruby_test_unit -Ilib:test tests

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%files
%doc CHANGELOG.md
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- Initial build for ALT Linux

