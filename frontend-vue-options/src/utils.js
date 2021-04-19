
export function propsConverter(route, component) {
    const props = { ...route.params };
    for (const key in props) {
        let value = props[key];
        if (!(value instanceof component.props[key].type)) {
            props[key] = component.props[key].type(value);
        }
    }
    return props;
}

