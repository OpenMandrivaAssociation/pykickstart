%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary:  A python library for manipulating kickstart files
Name: pykickstart
Url: http://fedoraproject.org/wiki/pykickstart
Version: 1.99.15
Release: 2
# This is a Red Hat maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
Source0: %{name}-%{version}.tar.gz

License: GPLv2
Group: Development/Python
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python-devel, gettext, python-setuptools
Requires: python, python-urlgrabber

%description
The pykickstart package is a python library for manipulating kickstart
files.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README ChangeLog COPYING docs/programmers-guide
%doc docs/kickstart-docs.txt
%{python_sitelib}/*
%{_bindir}/ksvalidator
%{_bindir}/ksflatten
%{_bindir}/ksverdiff

%changelog
* Thu Aug 09 2012 Chris Lumens <clumens@redhat.com> - 1.99.15-1
- No argument needs to be given to rootpw if you're just locking the account. (clumens)
