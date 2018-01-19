%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-horizon
Version:        10.6.0
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Horizon
License:        ASL 2.0

URL:            https://launchpad.net/puppet-horizon

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-apache
Requires:       puppet-stdlib
Requires:       puppet-memcached
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Horizon

%prep
%setup -q -n openstack-horizon-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/horizon/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/horizon/



%files
%{_datadir}/openstack-puppet/modules/horizon/


%changelog
* Fri Jan 19 2018 RDO <dev@lists.rdoproject.org> 10.6.0-1
- Update to 10.6.0

* Tue Nov 21 2017 RDO <dev@lists.rdoproject.org> 10.5.0-1
- Update to 10.5.0

* Wed Sep 20 2017 Alfredo Moralejo <amoralej@redhat.com> 10.4.0-1
- Update to 10.4.0

* Thu Apr 27 2017 rdo-trunk <javier.pena@redhat.com> 10.3.1-1
- Update to 10.3.1

* Fri Feb 10 2017 Alfredo Moralejo <amoralej@redhat.com> 10.3.0-1
- Update to 10.3.0


