%global import_path github.com/ceph/ceph-ansible

Name: ceph-ansible
Version: 6.0.28
Release: alt1

Summary: Ansible playbooks for Ceph
License: Apache-2.0
Group: Other
Url: https://%import_path

Source: %name-%version.tar
BuildArch: noarch

Requires: ansible
Requires: python3-module-netaddr

BuildRequires(pre): rpm-build-python3

%add_findprov_skiplist */library/*
%add_findreq_skiplist */library/*

%description
Ansible playbooks to deploy Ceph, the distributed filesystem.

%prep
%setup

%build

%install
mkdir -p %{buildroot}%{_datadir}/ceph-ansible

for f in ansible.cfg *.yml *.sample group_vars roles library module_utils plugins infrastructure-playbooks; do
  cp -a $f %{buildroot}%{_datadir}/ceph-ansible
done

pushd %{buildroot}%{_datadir}/ceph-ansible
  # These untested playbooks are too unstable for users.
  rm -r infrastructure-playbooks/untested-by-ci
popd

%files
%doc LICENSE README.rst docs
%{_datadir}/ceph-ansible

%changelog
* Mon Jun 05 2023 Stepan Paksashvili <paksa@altlinux.org> 6.0.28-alt1
- Initial build for ALT.
